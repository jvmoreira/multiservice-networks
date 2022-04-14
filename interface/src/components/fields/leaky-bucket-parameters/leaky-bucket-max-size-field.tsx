import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { LeakyBucketParameterFieldProps } from './leaky-bucket-parameters';

export function LeakyBucketMaxSizeField(props: LeakyBucketParameterFieldProps): ReactElement {
  const { leakyBucketParameters, setLeakyBucketParameters } = props;

  const leakyBucketMaxSize = useMemo(() => leakyBucketParameters.bucket_max_size || '', [leakyBucketParameters]);
  const setLeakyBucketMaxSize = useSetNfvTeFunctionParameter('bucket_max_size', setLeakyBucketParameters);
  const onLeakyBucketMaxSizeChangeHandler = useChangeHandler(setLeakyBucketMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket"
      name="bucket-max-size"
      value={leakyBucketMaxSize}
      placeholder="Valor em tokens"
      onChange={onLeakyBucketMaxSizeChangeHandler}
    />
  );
}
