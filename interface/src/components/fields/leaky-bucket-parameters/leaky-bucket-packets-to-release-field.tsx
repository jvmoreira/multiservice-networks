import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { LeakyBucketParameterFieldProps } from './leaky-bucket-parameters';

export function LeakyBucketPacketsToReleaseField(props: LeakyBucketParameterFieldProps): ReactElement {
  const { leakyBucketParameters, setLeakyBucketParameters } = props;

  const leakyBucketPacketsToRelease = useMemo(() => leakyBucketParameters.packets_to_release || '', [leakyBucketParameters]);
  const setLeakyBucketPacketsToRelease = useSetNfvTeFunctionParameter('packets_to_release', setLeakyBucketParameters);
  const onLeakyBucketPacketsToReleaseChangeHandler = useChangeHandler(setLeakyBucketPacketsToRelease);

  return (
    <FormInput
      label="Pacotes Transmitidos por Intervalo"
      name="interval"
      value={leakyBucketPacketsToRelease}
      onChange={onLeakyBucketPacketsToReleaseChangeHandler}
    />
  );
}
