import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { LeakyBucketParameterFieldProps } from './leaky-bucket-parameters';

export function LeakyBucketIntervalField(props: LeakyBucketParameterFieldProps): ReactElement {
  const { leakyBucketParameters, setLeakyBucketParameters } = props;

  const leakyBucketInterval = useMemo(() => leakyBucketParameters.interval || '', [leakyBucketParameters]);
  const setLeakyBucketInterval = useSetNfvTeFunctionParameter('interval', setLeakyBucketParameters);
  const onLeakyBucketIntervalChangeHandler = useChangeHandler(setLeakyBucketInterval);

  return (
    <FormInput
      label="Intervalo"
      name="interval"
      value={leakyBucketInterval}
      placeholder="Valor em segundos"
      onChange={onLeakyBucketIntervalChangeHandler}
    />
  );
}
